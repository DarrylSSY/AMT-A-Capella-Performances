<p align="center"><img src="https://socialify.git.ci/DarrylSSY/AMT-A-Capella-Performances/image?description=1&amp;font=Inter&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Plus&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<h1 align="center" id="title">Automatic Music Transcription: A Capella Performances</h1>
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Separate A Capella audio into Soprano, Alto, Bass, Tenor, Lead Vocal, and Vocal Percussion tracks via 4 methods:
    *    Non-negative Matrix Factorization (NMF)
    *    Independent Low Ranking Matrix Analysis (ILRMA)
    *    Convolutional Recurrent Neural Network with Attention (CRNN-A) model
    *    **Spleeter (best results)**

*   Convert WAV audio files to MIDI files (via signal processing techniques and probabilistic modelling)
*   Lyrics transcription from Lead Vocal track (via OpenAI’s Whisper)
*   Combine audio MIDI files and lyrics into sheet music (via music21 python library)

<h2>🛠️ Installation Steps:</h2>

**0. Download required datasets**<br>
a. Go to the following <a href="https://drive.google.com/drive/folders/1pSjRHzHAc97fRF-NB6P40o0Um8KyCUfZ">link</a>. <br>
b. Download the Ja Capella dataset zipped file. <br>
c. Rename your Ja Capella dataset zipped file to "Jacapella.zip" <br>
d. Upload it into this folder directory: "/Notebooks/Dataset" <br>

**1. Create environment**  
`python -m venv env`

**2. Activate environment**  
Windows: `env\Scripts\activate`  
Mac: `source env/bin/activate`

**3. Install kernel in environment**  
`pip install ipython`  
`pip install ipykernel`  
`ipython kernel install --user --name=env`

**4. To add new packages, add it in requirements and run**  
`pip install -r requirements.txt`

**5. To run jupyter notebook, run**  
`jupyter notebook`  
Ensure that you are using the kernel `env` by
clicking on  
`Kernel > Change kernel > env`


<h2>💻 Built with</h2>

Technologies used in the project:

*   Jupyter Notebook
*   Python
*   Spleeter by Deezer
*   Onset and Frames
*   ASR Models

<h2>🥳 Contributors</h2>
<table>
  <tbody>
    <tr>
<td align="center" valign="top">
        <a href="https://darrylssy.com"><img src="https://github.com/DarrylSSY.png"/>
        <br /><sub><b>Darryl Soh</b></sub></a></td>
<td align="center" valign="top">
        <a href="https://github.com/simyanyi"><img src="https://github.com/simyanyi.png"/>
        <br /><sub><b>Sim Yan Yi</b></sub></a></td>
<td align="center" valign="top">
        <a href=""><img src="https://github.com/identicons/mwhite.png"/>
        <br /><sub><b>Enqi Chan</b></sub></a></td>
<td align="center" valign="top">
        <a href=""><img src="https://github.com/identicons/mwhite.png"/>
        <br /><sub><b>Tay Wan Lin</b></sub></a></td>
<td align="center" valign="top">
        <a href=""><img src="https://github.com/identicons/mwhite.png"/>
        <br /><sub><b>Joel John Tan</b></sub></a></td>
<td align="center" valign="top">
        <a href=""><img src="https://github.com/identicons/mwhite.png"/>
        <br /><sub><b>Kruise Tog</b></sub></a></td>
<td align="center" valign="top">
        <a href=""><img src="https://github.com/identicons/mwhite.png"/>
        <br /><sub><b>Norman Ng</b></sub></a></td>
    </tr>
  </tbody>
</table>
