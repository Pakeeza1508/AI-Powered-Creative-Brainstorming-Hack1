import logging

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

responses_logger = logging.getLogger("AgentResponses")
responses_logger.setLevel(logging.INFO)
responses_logger.addHandler(handler)
responses_logger.propagate = False

errors_logger = logging.getLogger("AppErrors")
errors_logger.setLevel(logging.ERROR)
errors_logger.addHandler(handler)
errors_logger.propagate = False

debug_logger = logging.getLogger("AppDebug")
debug_logger.setLevel(logging.DEBUG)
debug_logger.addHandler(handler)
debug_logger.propagate = False