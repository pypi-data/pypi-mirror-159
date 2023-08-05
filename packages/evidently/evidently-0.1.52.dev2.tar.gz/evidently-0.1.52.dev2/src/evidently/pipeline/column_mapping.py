from typing import Optional, List, Union, Sequence

from dataclasses import dataclass


class TaskType:
    REGRESSION_TASK: str = "regression"
    CLASSIFICATION_TASK: str = "classification"


@dataclass
class ColumnMapping:
    target: Optional[str] = "target"
    prediction: Optional[Union[str, Sequence[str]]] = "prediction"
    datetime: Optional[str] = "datetime"
    id: Optional[str] = None
    numerical_features: Optional[List[str]] = None
    categorical_features: Optional[List[str]] = None
    datetime_features: Optional[List[str]] = None
    target_names: Optional[List[str]] = None
    task: Optional[str] = None

    def is_classification_task(self):
        return self.task == TaskType.CLASSIFICATION_TASK

    def is_regression_task(self):
        return self.task == TaskType.REGRESSION_TASK
