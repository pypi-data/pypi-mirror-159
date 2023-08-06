from typing import Dict, List, Optional, Union

from relevanceai.client.helpers import Credentials
from relevanceai.dataset.series import Series
from relevanceai.operations import Operations
from relevanceai.operations_new import Operations as OperationsNew
from relevanceai.utils.decorators.analytics import track
from relevanceai.constants import (
    GLOBAL_DATASETS,
    SEARCH_APP_LINK,
    PROJECTOR_APP_LINK,
    EXPLORER_APP_LINK,
)


class Dataset(OperationsNew, Operations):
    @track
    def __init__(
        self,
        credentials: Credentials,
        dataset_id: str,
        fields: Optional[list] = None,
        image_fields: Optional[List[str]] = None,
        audio_fields: Optional[List[str]] = None,
        highlight_fields: Optional[Dict[str, List]] = None,
        text_fields: Optional[List[str]] = None,
        **kwargs,
    ):
        self.credentials = credentials
        self.fields = [] if fields is None else fields
        self.dataset_id = dataset_id
        self.image_fields = [] if image_fields is None else image_fields
        self.audio_fields = [] if audio_fields is None else audio_fields
        self.highlight_fields = {} if highlight_fields is None else highlight_fields
        self.text_fields = [] if text_fields is None else text_fields

        super().__init__(
            credentials=credentials,
            dataset_id=self.dataset_id,
            fields=fields,
            image_fields=image_fields,
            audio_fields=audio_fields,
            highlight_fields=highlight_fields,
            text_fields=text_fields,
            **kwargs,
        )
        # add global datasets
        if self.dataset_id in GLOBAL_DATASETS:
            # avoid re-inserting if it already exists
            if self.shape[0] == 0:
                from relevanceai.utils.datasets import mock_documents
                from relevanceai.utils.decorators.analytics import fire_and_forget

                @fire_and_forget
                def add_mock_dataset():
                    self.upsert_documents(mock_documents(100))

                add_mock_dataset()
        self.is_empty()

    def is_empty(self):
        """Check if a dataset is empty."""
        try:
            if self.shape[0] == 0:
                try:
                    print("⚠️ Your dataset has no documents. Make sure to insert some!")
                except:
                    pass
        except:
            pass

    @track
    def __getitem__(self, field: Union[List[str], str]):
        """
        Returns a Series Object that selects a particular field within a dataset
        Parameters
        ----------
        field: Union[List, str]
            The particular field within the dataset
        Returns
        -------
        Tuple
            (N, C)
        Example
        ---------------
        .. code-block::

            from relevanceai import Client
            client = Client()
            dataset_id = "sample_dataset_id"
            df = client.Dataset(dataset_id)
            field = "sample_field"
            series = df[field]
        """
        if isinstance(field, str):
            return Series(
                credentials=self.credentials,
                dataset_id=self.dataset_id,
                field=field,
                image_fields=self.image_fields,
                audio_fields=self.audio_fields,
                highlight_fields=self.highlight_fields,
                text_fields=self.text_fields,
            )
        elif isinstance(field, list):
            return Dataset(
                credentials=self.credentials,
                dataset_id=self.dataset_id,
                fields=field,
                image_fields=self.image_fields,
                audio_fields=self.audio_fields,
                highlight_fields=self.highlight_fields,
                text_fields=self.text_fields,
            )
        else:
            raise TypeError("Field needs to be a list or a string.")

    @track
    def launch_search_app(self):
        """
        Launches the link to the search application to start building

        .. code-block::

            ds.launch_search_app()

        """
        print(SEARCH_APP_LINK.format(self.dataset_id))

    @track
    def launch_projector_app(self):
        """
        Launches the link to the projector application to start building

        .. code-block::

            ds.launch_projector_app()

        """
        print(PROJECTOR_APP_LINK.format(self.dataset_id))

    @track
    def launch_explore_app(self):
        print(EXPLORER_APP_LINK.format(self.dataset_id))

    def set_dtypes(self, mapping: dict):
        unstruc_types = ["_numeric_", "_category_", "_text_", "_image_"]
        for unstruc_type in unstruc_types:
            if unstruc_type not in mapping:
                mapping[unstruc_type] = []

        self.datasets.post_metadata(
            self.dataset_id,
            metadata=mapping,
        )

    def get_dtypes(self):
        metadata = self.datasets.metadata(
            self.dataset_id,
        )["results"]
        metadata = {
            key: value
            for key, value in metadata.items()
            if key.startswith("_") and key.endswith("_")
        }
        return metadata

    def label_clusters(self, cluster_labels: dict, alias: str, vector_fields: list):
        """
        Label your clusters programatiically

        Example
        ----------

        .. code-block::

            ds.label_clusters(
                {"cluster_1" : "nice reviews"},
                alias=...,
                vector_fields=...
            )

        """
        metadata = self.metadata
        metadata_doc = metadata.to_dict()

        if "cluster_metadata" not in metadata_doc:
            metadata_doc["cluster_metadata"] = {"labels": {}}

        cluster_field = "_cluster_." + ".".join(vector_fields) + "." + alias

        if cluster_field not in metadata_doc["cluster_metadata"]["labels"]:
            labels = metadata_doc["cluster_metadata"]["labels"]
            labels.update({cluster_field: {"labels": cluster_labels}})
        else:
            metadata_doc["cluster_metadata"]["labels"][cluster_field][
                "labels"
            ] = cluster_labels
        return self.upsert_metadata(metadata_doc)
