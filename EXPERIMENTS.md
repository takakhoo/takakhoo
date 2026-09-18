# Experiments you can run

A guide to the public code behind my portfolio. Start with a repository's README
for its exact environment, command and data requirements, then inspect the saved
outputs and automated run. Results below are bounded experiments, not claims
that every historical thesis-scale study has been rerun.

## Start here

- **Build and hear something:** [a C music generator with rendered audio](https://github.com/takakhoo/algorithmic-music-generator), or [seeded chord/rhythm MIDI](https://github.com/takakhoo/generative-music-algorithms).
- **Inspect an implementation against an independent baseline:** [dual SVM versus LibSVM](https://github.com/takakhoo/svm-dual-optimization).
- **Explore a failure mode:** [noise amplification in a pseudoinverse](https://github.com/takakhoo/svd-pseudoinverse-lab), or [why fitting gradients does not guarantee recovering inputs](https://github.com/takakhoo/federated-asr-update-reconstruction).
- **Follow a learning curve:** [notebook autoencoder and tiny Transformer](https://github.com/takakhoo/machine-learning-labs).

## Numerical methods

| Repository | What to explore | Evidence and scope |
|---|---|---|
| [gradient-descent-lab](https://github.com/takakhoo/gradient-descent-lab) | Optimizer stability across condition numbers; fixed versus adaptive steps | [Saved results](https://github.com/takakhoo/gradient-descent-lab/tree/main/results) · [Verified run](https://github.com/takakhoo/gradient-descent-lab/actions/runs/35304700168). Deterministic quadratic diagnostic. |
| [svd-pseudoinverse-lab](https://github.com/takakhoo/svd-pseudoinverse-lab) | Pseudoinverse reconstruction and noise amplification; truncation versus unstable inversion | [Saved results](https://github.com/takakhoo/svd-pseudoinverse-lab/tree/main/results) · [Verified run](https://github.com/takakhoo/svd-pseudoinverse-lab/actions/runs/35304896135). Synthetic ill-conditioned system. |
| [probability-clt-lab](https://github.com/takakhoo/probability-clt-lab) | Exact interval coverage, estimator risk and a rare-event CLT counterexample | [Saved results](https://github.com/takakhoo/probability-clt-lab/tree/main/results) · [Verified run](https://github.com/takakhoo/probability-clt-lab/actions/runs/35306554982). Seeded Monte Carlo plus exact calculation. |
| [svm-dual-optimization](https://github.com/takakhoo/svm-dual-optimization) | Hand-built dual SVM compared with LibSVM; 98.67% held-out digits accuracy | [Saved results](https://github.com/takakhoo/svm-dual-optimization/tree/main/results) · [Verified run](https://github.com/takakhoo/svm-dual-optimization/actions/runs/35306864080). 8×8 digits, not MNIST; validation-only tuning. |
| [markov-image-restoration](https://github.com/takakhoo/markov-image-restoration) | Noisy-image restoration versus exact graph cuts, including thin-structure failure | [Saved results](https://github.com/takakhoo/markov-image-restoration/tree/main/results) · [Verified run](https://github.com/takakhoo/markov-image-restoration/actions/runs/35305617509). 54-case diagnostic; no clean-target restart selection. |
| [geometric-multiresolution-analysis](https://github.com/takakhoo/geometric-multiresolution-analysis) | Held-out manifold reconstruction and forward/inverse consistency | [Saved results](https://github.com/takakhoo/geometric-multiresolution-analysis/tree/main/results) · [Verified run](https://github.com/takakhoo/geometric-multiresolution-analysis/actions/runs/35307572272). Synthetic helix; local models use more storage than global PCA. |
| [machine-learning-labs](https://github.com/takakhoo/machine-learning-labs) | Notebook autoencoder and tiny Transformer learn on held-out patches/text | [Saved results](https://github.com/takakhoo/machine-learning-labs/tree/main/results/cpu) · [Verified run](https://github.com/takakhoo/machine-learning-labs/actions/runs/35312921058). Bounded CPU training; some historical course labs remain templates. |

## Music and audio

| Repository | What to explore | Evidence and scope |
|---|---|---|
| [neural-audio-restoration](https://github.com/takakhoo/neural-audio-restoration) | Three-seed architecture ablation with learning curves and checkpoint checks | [Saved results](https://github.com/takakhoo/neural-audio-restoration/tree/main/results/cpu-ablation) · [Verified run](https://github.com/takakhoo/neural-audio-restoration/actions/runs/35305359363). Synthetic codec-token task, not a mastering-quality result. |
| [transformer-melody-generation](https://github.com/takakhoo/transformer-melody-generation) | Causal sequence training, bigram comparison, seeded MIDI and checkpoint reload | [Saved results](https://github.com/takakhoo/transformer-melody-generation/tree/main/results) · [Verified run](https://github.com/takakhoo/transformer-melody-generation/actions/runs/35306487459). Small held-out melody set; bigram beats the overfit Transformer. |
| [generative-music-algorithms](https://github.com/takakhoo/generative-music-algorithms) | Seeded rhythm/chord MIDI and genetic search checked against exact enumeration | [Saved results](https://github.com/takakhoo/generative-music-algorithms/tree/main/results) · [Verified run](https://github.com/takakhoo/generative-music-algorithms/actions/runs/35307166768). Handwritten fitness is not a musical-quality score. |
| [algorithmic-music-generator](https://github.com/takakhoo/algorithmic-music-generator) | Seeded C score generator, rendered Csound audio, sanitizers and timing tests | [Saved results](https://github.com/takakhoo/algorithmic-music-generator/tree/main/results) · [Verified run](https://github.com/takakhoo/algorithmic-music-generator/actions/runs/35308119817). Real rendered audio; no listening-quality benchmark. |
| [sparse-music-source-separation](https://github.com/takakhoo/sparse-music-source-separation) | Train/held-out source separation with WAVs and an overlapping-band failure case | [Saved results](https://github.com/takakhoo/sparse-music-source-separation/tree/main/results/synthetic) · [Verified run](https://github.com/takakhoo/sparse-music-source-separation/actions/runs/35308547458). Synthetic mixtures, not the full MUSDB18 study. |
| [audio-diffusion-control](https://github.com/takakhoo/audio-diffusion-control) | Audible DSP controls, measured descriptors and held-out PCA reconstruction | [Saved results](https://github.com/takakhoo/audio-diffusion-control/tree/main/results/descriptor-demo) · [Verified run](https://github.com/takakhoo/audio-diffusion-control/actions/runs/35308548431). DSP demonstration; diffusion/CLAP/LoRA remain placeholders. |
| [mnist-to-music-unet](https://github.com/takakhoo/mnist-to-music-unet) | U-Net versus classifier/DSP digit-to-audio comparison, with listenable outputs | [Saved results](https://github.com/takakhoo/mnist-to-music-unet/tree/main/results/cpu) · [Verified run](https://github.com/takakhoo/mnist-to-music-unet/actions/runs/35309961219). Bundled 8×8 digits; classifier/DSP wins this budget. |
| [sonic-pi-composer-agents](https://github.com/takakhoo/sonic-pi-composer-agents) | Correlated OSC feedback, failed-code correction and provider-adapter traces | [Saved results](https://github.com/takakhoo/sonic-pi-composer-agents/tree/main/results/offline) · [Verified run](https://github.com/takakhoo/sonic-pi-composer-agents/actions/runs/35309129920). Scripted offline replay; live LLM/Sonic Pi run is separate. |

## Systems and evaluation

| Repository | What to explore | Evidence and scope |
|---|---|---|
| [datago-retrieval-search](https://github.com/takakhoo/datago-retrieval-search) | Cosine retrieval consistency and an adversarial-tree MCTS budget sweep | [Saved results](https://github.com/takakhoo/datago-retrieval-search/tree/main/results/core) · [Verified run](https://github.com/takakhoo/datago-retrieval-search/actions/runs/35309526637). Component tests, not Go matches or an AlphaGo comparison. |
| [federated-asr-gradient-inversion](https://github.com/takakhoo/federated-asr-gradient-inversion) | Higher-order CTC checks and a three-seed gradient-inversion diagnostic | [Saved results](https://github.com/takakhoo/federated-asr-gradient-inversion/tree/main/reports/cpu-diagnostic) · [Verified run](https://github.com/takakhoo/federated-asr-gradient-inversion/actions/runs/35310476813). Synthetic known-label features; good gradient fit need not recover input. |
| [federated-asr-update-reconstruction](https://github.com/takakhoo/federated-asr-update-reconstruction) | Full-rank, underdetermined and noisy feature reconstruction with ridge baselines | [Saved results](https://github.com/takakhoo/federated-asr-update-reconstruction/tree/main/results/ls) · [Verified run](https://github.com/takakhoo/federated-asr-update-reconstruction/actions/runs/35310833921). Needs per-frame logit gradients, not ordinary FedAvg updates alone. |
| [parsere-elf-evaluation](https://github.com/takakhoo/parsere-elf-evaluation) | 20 benign ELF fixtures, parser checks and hosted QEMU trace artifacts | [Saved results](https://github.com/takakhoo/parsere-elf-evaluation/tree/main/results/fixtures.json) · [Verified run](https://github.com/takakhoo/parsere-elf-evaluation/actions/runs/35312873429). Translation-order graph is not a full execution CFG; old manual accuracy not revalidated. |
| [prediction-market-research-agent](https://github.com/takakhoo/prediction-market-research-agent) | Strict probability/schema contracts and an eight-case matcher replay | [Saved results](https://github.com/takakhoo/prediction-market-research-agent/tree/main/results/offline-replay.json) · [Verified run](https://github.com/takakhoo/prediction-market-research-agent/actions/runs/35312559902). No live trades, paid model calls or semantic-accuracy claim. |
| [llm-security-research-library](https://github.com/takakhoo/llm-security-research-library) | Searchable offline reference catalog, source links, hashes and license flags | [Saved results](https://github.com/takakhoo/llm-security-research-library/tree/main/catalog) · [Verified run](https://github.com/takakhoo/llm-security-research-library/actions/runs/35312028978). 58 references; vendored code is not executed or independently certified. |
| [pomdp-regime-allocation](https://github.com/takakhoo/pomdp-regime-allocation) | Chronological HMM/QMDP allocation versus 60/40 and trend baselines | [Saved results](https://github.com/takakhoo/pomdp-regime-allocation/tree/main/results/chronological) · [Verified run](https://github.com/takakhoo/pomdp-regime-allocation/actions/runs/35311848325). Historical snapshot, not point-in-time data; corrected QMDP trails 60/40. |

## What reproducible means here

- The README defines a bounded path with dependencies, inputs, seeds where relevant,
  and expected output locations. Generated plots, metrics, audio or traces make
  the result inspectable without taking the headline on trust.
- Tests guard the implementation changes; linked GitHub runs record the tested
  revision. A passing component test is not a full product or research validation.
- Baselines and unsuccessful outcomes stay visible. Synthetic diagnostics are
  labeled separately from real datasets, historical results and unimplemented work.
- Larger speech/audio experiments can still require external datasets, licensed
  assets, trained checkpoints or GPU resources. Those limits belong in each README.

[Résumé](resume/Taka_Khoo_Resume.pdf) · [Portfolio](https://takakhoo.com)
