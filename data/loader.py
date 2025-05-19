import yaml
import pandas as pd

class DataLoader:
    def __init__(self, config_path="config.yaml", dataset_name="laptops.csv"):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

        # Dynamically inject dataset name into path
        self.config['data_path'] = self.config['data_path'].format(dataset_name=dataset_name)

        # Try with 'latin1' encoding
        try:
            self.df = pd.read_csv(self.config['data_path'], encoding='latin1')
        except UnicodeDecodeError:
            # If 'latin1' fails, try 'cp1252'
            self.df = pd.read_csv(self.config['data_path'], encoding='cp1252')

        self._clean_data_numerics()
        self._build_stringified_fields()
        self._build_description()

    def _clean_data_numerics(self):
        for field in self.config['numeric_fields']:
            self.df[field] = (
                self.df[field]
                .astype(str)
                .str.replace(",", ".", regex=False)
                .str.extract(r"([\d\.]+)")[0]
                .astype(float)
            )

    def _build_stringified_fields(self):
        for field in self.config['numeric_fields']:
            str_field = f"{field}_str"
            self.df[str_field] = self.df[field].fillna(-1).apply(
                lambda x: f"{x} {field}" if x != -1 else f"{field} not determined"
            )

    def _build_description(self):
        all_fields = self.config['key_fields']
        self.df[self.config['output_field']] = self.df[all_fields].astype(str).agg(", ".join, axis=1)

    def get_data(self):
        return self.df[[self.config['id_field'], self.config['output_field']]]

    def get_full_df(self):
        return self.df


