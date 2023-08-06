"""Abstract class for huggingface exporters."""
from abc import abstractmethod

from loguru import logger
from npc_engine_import_wizard.import_wizards.base_import_wizard import ImportWizard
import click
from transformers import AutoTokenizer
import sys


class BaseHfImportWizard(ImportWizard):
    """ImportWizard for the Huggingface transformer models."""

    def convert(self, model_path: str, export_path: str):
        """Export the model to the export path."""
        click.echo("Exporting model to onnx")
        sys.argv = [
            "onnx_converter",
            "--model",
            model_path,
            "--atol",
            "0.0001",
            "--feature",
            self.get_export_feature(),
            export_path,
        ]
        from transformers.onnx import __main__

        __main__.logger = logger
        __main__.main()
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        tokenizer.save_pretrained(export_path)

    @abstractmethod
    def get_export_feature(self) -> str:
        """Get the transformers.onnx feature argument that describes what interface model should have.

        Possible values are:
            'causal-lm', 'causal-lm-with-past', 'default', 'default-with-past', 'masked-lm',
            'question-answering', 'seq2seq-lm', 'seq2seq-lm-with-past', 'sequence-classification',
            'token-classification'
        """
        pass
