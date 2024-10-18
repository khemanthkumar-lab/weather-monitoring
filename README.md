# weather-monitoring
Real-Time Weather Monitoring System

## Objective
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates from the OpenWeatherMap API.

## Features
- Fetches weather data for multiple cities in India.
- Converts temperature from Kelvin to Celsius.
- Provides alerts based on user-defined temperature thresholds.
- Scheduled data fetching every 5 minutes.
- Daily weather summaries (averages, max/min, dominant weather).

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Dependencies
The following Python libraries are required:
- `requests`
- `schedule`
- `matplotlib` (for visualization)

You can install these libraries using the following command:
```bash
pip install requests schedule matplotlib
