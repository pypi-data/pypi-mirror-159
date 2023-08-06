# Streamn Python SDK

This [Streamn](https://www.streamn.ai) Python SDK provides convenient access to the Streamn API's.

## Documentation

See the [API docs](https://docs.streamn.ai/)

### Requirements

- Python 3+

## Installation

First make sure that Python is installed in your system.

```sh
pip install --upgrade streamn
```

<!-- > install using github repo:

```
1. clone this repo
2. move the repo ( cd alignment )
3. create virtual env(python3 -m venv virtualenvName)
4. activate the virtualenv ( source virtualenvName/bin/activate)
5. install required libraries ( pip3 install -r requirements.txt )
6. call the required fucntion from the utils file and add it in your code 
``` -->

## Configuration

The library needs to be configured with your account's API Key

save credentials by saving a file named streamn_config.json in your working directory in the following format.

Example of 'streamn_cofig.json' file

```conf
{
    "api_key":"asaisdniasnasnfjasdfn_asjhnadjsdsa"
}
```
## A Transcript generation Example


```python
import streamnai

# Process audio file
status , transcipt = streamnai.process_audio.transcribe_audio( audio_file_path = <audio file path to transcibe> , is_medical = <bool, True or Flase> , vocabulary_name = <string, vocab name>  , LanguageModelName = <string,language model name >  )

```
## A Transcript with Audiolab scores generation Example

```python
import streamnai

# Process audio file
status , transcipt = streamnai.process_audio.get_audiolab_transcript(audio_file_path = <audio file path to transcibe> , is_medical = <bool, True or Flase> , vocabulary_name = <string, vocab name>  , LanguageModelName = <string,language model name >  )

```

## A Improved Transcript generation Example

```python
import streamnai

# Process audio file
status , transcipt = streamnai.process_audio.get_improved_transcript( audio_file_path = <audio file path to transcibe> , is_medical = <bool, True or Flase> , vocabulary_name = <string, vocab name>  , LanguageModelName = <string,language model name >  )

```

To know more about these functions and parameters, click [here][extended-readme-functions-object]



## Need support

If the above doesn't help, do let us know at contact@streamn.ai

[symbl-docs]: https://docs.streamn.ai/
[extended-readme-functions-object]: https://github.com/saireddy12/streamn_sdk/blob/main/src/streamnai/README.md