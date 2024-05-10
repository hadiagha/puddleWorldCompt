# Puddle-World

Welcome to the Puddle-World repository, dedicated to Reinforcement Learning for the Upper Bound 2024 competition. I'm Hadi Aghazadeh, and I'm excited to participate in this event with a scholarship. Here, I'll outline the purpose, methodologies, results, and more regarding my approach to tackling the Puddle World problem.

## Table of Contents

- [Description](#description)
- [Run](#run)
- [Score](#score)
- [About](#about)
- [License](#license)

## Description

The Puddle World problem poses challenges in Reinforcement Learning due to its continuous state space. In this project, I experimented with various algorithms and strategies to find effective solutions. Initially, I explored stable baseline models and discovered the importance of devising robust state representation methods.

Drawing from my knowledge gained in the Reinforcement Learning specialization on Coursera, particularly focusing on Tile Coding, I began with this technique and achieved promising results. However, further refinement led me to the adoption of Kanerva state representation, which significantly improved overall scores and stability.

Pushing the boundaries of existing methodologies, I devised my own technique named "Adaptive Kanerva Coder." While this outperformed Kanerva slightly, its computational complexity prompted me to stick with Kanerva for the competition. Nevertheless, I eagerly await the opportunity to discuss and present this novel approach.

I also experimented with Radial Basis Function (RBF) state representation, albeit with less success. Given more time, I believe refining this approach could yield better results.

Regarding models, I explored a range including Tabular SARSA, Tabular Q-Learning, Deep Q Learning, and variants with Eligibility Trace. Additionally, I delved into advanced models like Option Learning and MAXQ, though time constraints limited their optimization.

After extensive trial and error, I settled on Tabular Q-Learning for its superior performance in maximizing rewards. Notably, Tabular Q-Learning with Eligibility Trace showed comparable results.

## Run

The primary code for obtaining results is located in `submissionCode.ipynb`. It comprises two parts: one for obtaining results without parameter tuning, offering faster execution, and another for achieving the best results submitted for the competition, albeit requiring considerable time due to parameter tuning.

All experiments are documented in separate notebooks, providing accessibility and insights. Video outputs are available for these experiments. Notably, the latest experiment for Kanerva and Adaptive Kanerva can be found in `hands_on_experiments6.ipynb`.

## Score

My scores in the competition varied based on the techniques employed. With Tile Coding, I achieved a score of -34. This improved to -31 with Kanerva Coder and further to -30.7 through parameter fine-tuning, representing the best result I obtained.

## About

I am Hadi Aghazadeh, a PhD student at the University of Calgary, specializing in applying Reinforcement Learning to supply chain, routing, and scheduling problems. I've already contributed to research in the intersection of RL and intermodal transportation, with one paper published and another major work accepted in the Journal of Transportation Research Part C (Impact Factor=8.3). The title of my paper is "Dray_Q: Demand Depended Trailer Repositioning using Deep Reinforcement Learning."

## License

This project is licensed under the MIT License.
