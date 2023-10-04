from loguru import logger

# 로거 설정
logger.add(
    "logs/{time:YYYY-MM-DD}.log", 
    rotation="1 day",  # 매일 로테이션
    retention="180 days",  # 180일 보관
    compression="zip"  # 압축 형식
)

def get_logger():
    return logger