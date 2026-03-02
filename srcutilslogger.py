"""
Unified logging system with Firebase integration for real-time monitoring
"""
import logging
import sys
from typing import Dict, Any, Optional
from datetime import datetime
import traceback

from loguru import logger
from firebase_admin import firestore

class TradingLogger:
    """Centralized logging with Firebase Firestore integration"""
    
    def __init__(self, firestore_client: Optional[firestore.Client] = None):
        """
        Initialize logger with optional Firebase integration
        
        Args:
            firestore_client: Firebase Firestore client for cloud logging
        """
        self.firestore_client = firestore_client
        self.setup_loguru()
        
    def setup_loguru(self) -> None:
        """Configure Loguru logger with structured formatting"""
        logger.remove()  # Remove default handler
        
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
            "<level>{message}</level>"
        )
        
        # Console output
        logger.add(
            sys.stdout,
            format=log_format,
            level="INFO",
            colorize=True
        )
        
        # File output
        logger.add(
            "logs/trading_{time:YYYY-MM-DD}.log",
            format=log_format,
            level="DEBUG",
            rotation="1 day",
            retention="30 days",
            compression="zip"
        )
        
    def log_trade(
        self,
        trade_data: Dict[str, Any],
        level: str = "INFO"
    ) -> None:
        """
        Log trade execution with comprehensive metadata
        
        Args:
            trade_data: Dictionary containing trade details
            level: Log level (INFO, WARNING, ERROR)
        """
        log_entry = {
            **trade_data,
            "timestamp": datetime.utcnow().isoformat(),
            "type": "trade_execution"
        }
        
        # Log to console/file
        getattr(logger, level.lower())(
            f"Trade