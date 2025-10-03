# Stock Trading ML

This project is connected to the other two repositories. Different repos for better encapsulation, since these projects will be run on separate Proxmox containers: 

[Trade Frontend](https://github.com/sudo-JP/Stock-Trading-Trade)

[Database](https://github.com/sudo-JP/Stock-Trading-DB)

Current architecure. Project is still in progress, so lots of empty files for now. 

```bash
.
├── compose.yaml
├── Dockerfile
├── LICENSE
├── requirements.txt
└── src
    ├── configs
    │   ├── base.yaml
    │   ├── feature_config.yaml
    │   ├── __init__.py
    │   ├── model_config.yaml
    │   └── trading_config.yaml
    ├── data
    │   └── __init__.py
    ├── evaluation
    │   ├── attribution.py
    │   ├── backtest_analyzer.py
    │   ├── drift_detector.py
    │   ├── __init__.py
    │   └── metrics.py
    ├── features
    │   ├── __init__.py
    │   ├── microstructure.py
    │   ├── regime_detection.py
    │   ├── statistical.py
    │   └── technical.py
    ├── __init__.py
    ├── main.py
    ├── models
    │   ├── base_model.py
    │   ├── __init__.py
    │   ├── model_factory.py
    │   ├── model_registry.py
    │   ├── persistence
    │   │   ├── __init__.py
    │   │   ├── model_loader.py
    │   │   ├── model_saver.py
    │   │   └── version_manager.py
    │   ├── predictors
    │   │   ├── batch_predictor.py
    │   │   ├── ensemble_predictor.py
    │   │   ├── __init__.py
    │   │   └── realtime_predictor.py
    │   └── trainers
    │       ├── base_trainer.py
    │       ├── batch_trainer.py
    │       ├── __init__.py
    │       ├── online_trainer.py
    │       └── walkforward_trainer.py
    ├── network
    │   ├── clients
    │   │   ├── api_client.py
    │   │   ├── database_client.py
    │   │   └── prediction_client.py
    │   ├── __init__.py
    │   ├── publishers
    │   │   ├── alert_publisher.py
    │   │   └── market_data_subscriber.py
    │   └── subscribers
    │       ├── prediction_publisher.py
    │       └── trade_subscriber.py
    ├── orchestration
    │   ├── data_sync.py
    │   ├── health_check.py
    │   ├── __init__.py
    │   ├── live_trading.py
    │   └── retraining.py
    ├── real_time
    │   ├── feature_stream.py
    │   ├── inference_engine.py
    │   ├── __init__.py
    │   ├── risk_monitor.py
    │   └── signal_generate.py
    ├── training
    │   └── __init__.py
    └── utils
        └── __init__.py
```
