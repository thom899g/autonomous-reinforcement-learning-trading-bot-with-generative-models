autonomous_trading_bot/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── __init__.py
│   ├── constants.py
│   ├── firebase_config.json
│   └── trading_config.yaml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── collector.py
│   │   ├── preprocessor.py
│   │   └── synthetic_generator.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── rl_agent.py
│   │   ├── gan_model.py
│   │   └── ensemble_predictor.py
│   ├── trading/
│   │   ├── __init__.py
│   │   ├── environment.py
│   │   ├── broker.py
│   │   └── risk_manager.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── firebase_client.py
│   │   └── performance_tracker.py
│   └── api/
│       ├── __init__.py
│       └── telegram_bot.py
└── tests/
    ├── __init__.py
    ├── test_rl_agent.py
    └── test_risk_manager.py