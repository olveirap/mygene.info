from .ensembl_base import EnsemblParser
import biothings.dataload.uploader as uploader

class EnsemblAccUploader(uploader.MergerSourceUploader):

    name = "ensembl_acc"
    main_source = "ensembl"

    def load_data(self, data_folder):
        ep = EnsemblParser(data_folder)
        ensembl2acc = ep.load_ensembl2acc()
        return ensembl2acc

    def get_mapping(self):
        mapping = {
                "ensembl": {
                    "dynamic": False,
                    #"path": "just_name",
                    "properties": {
                        "transcript": {
                            "type": "string",
                            "analyzer": "string_lowercase",
                            },
                        "gene": {
                            "type": "string",
                            "analyzer": "string_lowercase",
                            },
                        "protein": {
                            "type": "string",
                            "analyzer": "string_lowercase",
                            },
                        'translation': {
                            "type": "object",
                            "enabled": False,
                            "include_in_all": False,
                            },
                        }
                    }
                }
        return mapping
