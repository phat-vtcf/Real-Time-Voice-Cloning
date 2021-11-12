##THIS CODE WILL NOT WORK IN GOOGLE COLAB
##MUST BE DONE IN THE TERMINAL (LOCAL ENVIRONMENT)
##IT WILL NOT SUPPORT MP3 FILES, WAV WORK WELL


##To make sure that all necessary packages were installed,
##even in case it didn't work with the requirements file, we added them here too

##pip install torch torchaudio tochvision
##pip install -r requirements.txt
##pip install librosa sounddevice umap unidecode inflect ffmpeg matplotlib PyQt5


# Use this demo to test the configurations in the terminal
# We added the "--no_mp3_support" because otherwise it gave an error
python demo_cli.py --no_mp3_support

# Use this code to actually open the toolbox application & have fun!
python demo_toolbox.py --no_mp3_support
