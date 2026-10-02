# Taka Khoo

**[Résumé (PDF)](resume/Taka_Khoo_Resume.pdf)** · **[Runnable experiments & results](EXPERIMENTS.md)** · **[Portfolio](https://takakhoo.com)** · [LinkedIn](https://www.linkedin.com/in/takakhoo/)

AI and product engineer building creative tools, applied machine-learning systems,
and production software. I have shipped music products used at scale, built
research prototypes for DARPA INGOTS with NARF Industries and Dartmouth's LISP
Lab, and completed theses spanning an AI-native DAW, neural audio
restoration, and music composition and production.

My work centers on music, machine learning, signal processing, and product
engineering. I care about systems that are useful beyond a demo: clear
evaluation, honest limitations, human review where it matters, and documentation
that lets another engineer reproduce the result.

## Selected work

- **[MODULO](https://takakhoo.com)** — an AI-native desktop music workstation developed as my M.S. thesis and product research platform.
- **[Audio Sliders](https://github.com/takakhoo/audio-diffusion-control)**: slider controls for text-to-music diffusion. Small LoRAs on ACE-Step 1.5 and Stable Audio Open that move the mood, harmony, groove, or brightness of a generated piece, each scored against measured audio descriptors and a music-quality model.
- **[Lacquer](https://github.com/takakhoo/lacquer)**: automatic restoration and mastering for finished mixes. DSP echo removal, a fine-tuned band-split transformer for reverb, a decision layer that reports what it changed, and a full log of what worked and what did not. Successor to my [honors thesis](https://github.com/takakhoo/neural-audio-restoration) on token-based restoration.
- **[Mikiri](https://github.com/takakhoo/mikiri-beats-katago)**: a learned stopping rule that beats KataGo, the strongest open-source Go engine in the AlphaGo line, using KataGo's own network. It decides move by move when the search has seen enough, and at the same search budget it wins 79% of the points over 1,000 games (+228 Elo). Successor to DataGo.
- **[Unsplice](https://github.com/takakhoo/unsplice)**: exact recovery of speech from federated ASR updates. One gradient from a speech recognizer gives back the client's features in closed form (98.5% of 1,417 LibriSpeech utterances up to 6.2 s, sequential decoding up to 35 s), with no transcript and no optimisation; Whisper reads the reconstructed audio at 3.8% WER. Replaces my earlier [gradient-matching attack](https://github.com/takakhoo/federated-asr-gradient-inversion).
- **[Prediction-market research agent](https://github.com/takakhoo/prediction-market-research-agent)** — human-reviewed evidence discovery and monitoring for prediction-market research.
- **[Transformer melody generation](https://github.com/takakhoo/transformer-melody-generation)** — a readable TensorFlow encoder–decoder Transformer for symbolic music generation.

For saved plots, MIDI/audio, baselines, test runs and honest experiment limits,
start with the [22-project reproducibility index](EXPERIMENTS.md).

## Engineering focus

`Python` · `TypeScript` · `C++` · `PyTorch` · `React` · `Node.js` · `PostgreSQL` · `Docker` · `GCP` · `JUCE` · `DSP`

My recent work includes real-time collaborative products, audio-model evaluation, LLM tool and agent systems, and graduate machine-learning instruction.

## Elsewhere

- Portfolio and writing: [takakhoo.com](https://takakhoo.com)
- LinkedIn: [linkedin.com/in/takakhoo](https://www.linkedin.com/in/takakhoo)
- Research paper: [Reconstructing Long-Form Speech from Federated ASR Gradients](https://takakhoo.com/docs/federated-asr-gradient-paper.pdf)
