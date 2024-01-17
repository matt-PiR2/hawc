from django import forms
from django.forms import ModelForm

from ..common.forms import BaseFormHelper, QuillField
from . import models


class ExperimentForm(ModelForm):
    class Meta:
        model = models.Experiment
        exclude = ("study",)
        field_classes = {"comments": QuillField}

    def __init__(self, *args, **kwargs):
        parent = kwargs.pop("parent", None)
        super().__init__(*args, **kwargs)
        if parent:
            self.instance.study = parent

        # change checkbox to select box
        self.fields["has_multiple_generations"].widget = forms.Select(
            choices=((True, "Yes"), (False, "No"))
        )

    @property
    def helper(self):
        # by default take-up the whole row
        for fld in list(self.fields.keys()):
            widget = self.fields[fld].widget
            if type(widget) != forms.CheckboxInput:
                widget.attrs["class"] = "form-control"

        if self.instance.id:
            inputs = {
                "legend_text": f"Update {self.instance}",
                "help_text": "Update an existing experiment.",
                "cancel_url": self.instance.get_absolute_url(),
            }
        else:
            inputs = {
                "legend_text": "Create new experiment",
                "help_text": """
                    Create a new experiment. Each experiment is a associated with a
                    study, and may have one or more collections of animals. For
                    example, one experiment may be a 2-year cancer bioassay,
                    while another multi-generational study. It is possible to
                    create multiple separate experiments within a single study,
                    with different study-designs, durations, or test-species.""",
                "cancel_url": self.instance.study.get_absolute_url(),
            }

        helper = BaseFormHelper(self, **inputs)

        helper.add_row("design", 2, "col-md-4")
        helper.form_id = "experiment-v2-form"
        return helper
