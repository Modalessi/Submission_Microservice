from enum import Enum


class SubmissionStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class SubmissionResult(Enum):
    WRONG_ANSWER = "wrong_answer"
    TIME_LIMIT_EXCEEDED = "time_limit_exceeded"
    MEMORY_LIMIT_EXCEEDED = "memory_limit_exceeded"
    ACCEPTED = "accepted"
    RUNTIME_ERROR = "runtime_error"
    COMPILATION_ERROR = "compilation_error"
