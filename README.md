# yai_2023winter_toy_project

Youtube thumbnail dataset generator ... by younghanstark

## Requirements
```bash
pip install google-api-python-client
```

## File Explanation
- `/thumbnails`: (Ignored) Dataset folder.
- `.gitignore`
- `balanceData.py`: A code can be used to balance dataset.
- `categories.py`: A code retrieves available video categories in US.
- `channels.pickle`: A pickle file that saves type 'set' contains channels already processed.
- `getChannels.py`: A code that retrieves random channel ids.
- `key.txt`: (Ignored) A text file that should contain your API key.
- `makeData.py`: A code that makes dataset from a list of channel ids.
- `metadata.csv`: Metadata of dataset.
- `README.md`: Me myself! :)

## Usage
1. Get your API key(Youtube Data API v3) on Google Cloud Platform
2. Run `getChannels.py` to get a list of random channel ids.
3. Run `makeData.py` to make dataset.
4. Carefully inspect your dataset and balance your dataset using `balanceData.py`.

## Note
- Always think of your quota limit. Especially `balanceData.py` uses large amount of quota points.