# Related work and positioning

This section preserves the manuscript's stated positioning. The contribution is deliberately narrow: the paper does not claim that topology variability, physics-informed GNNs, or graph attention are new. Its focus is strict topology-disjoint train/test separation and degradation as a continuous structural-distance quantity, with an observable-only re-analysis.

## Closest-work positioning from the paper

| Work | Topology variation | Physics | Primary emphasis stated in manuscript |
|---|---|---|---|
| Ngo et al. (2024) | Yes | Yes | Physics-informed graphical state estimation |
| Moshtagh et al. (2025) | Yes | No / limited | Topology-aware GNN for PMU-unobservable state estimation |
| Wu et al. (2025) | Yes | Yes | Meta-learning for topology variability |
| Haug and Goebel (2025) | Yes | No | Broad ML / distribution-system state-estimation benchmarking |
| This work (2026) | Strict held-out | Yes | Structural-OOD reliability and degradation versus topology distance |

The manuscript explicitly treats prior topology-aware GNN, physics-informed, and DSSE benchmarking work as complementary rather than claiming priority for those broad ideas.

## References

The following bibliography is transcribed from the paper's reference list.

1. Ali Abur and Antonio G. Expósito. 2004. *Power System State Estimation: Theory and Implementation*. Marcel Dekker.
2. Antonio S. Do Coutto Filho and Maria B. C. S. Trindade. 2019. Roots, achievements, and prospects of power system state estimation: A review on handling corrupted measurements. *International Transactions on Electrical Energy Systems*, 29(1), e2779. https://doi.org/10.1002/etep.2779
3. William L. Hamilton, Zhitao Ying, and Jure Leskovec. 2017. Inductive representation learning on large graphs. *Advances in Neural Information Processing Systems*, 30.
4. Theodor Haug and Christoph Goebel. 2025. DSML: A comprehensive framework for evaluating ML methods for distribution system state estimation. *Proceedings of the 16th ACM International Conference on Future and Sustainable Energy Systems*. https://doi.org/10.1145/3679240.3734629
5. Thomas N. Kipf and Max Welling. 2017. Semi-supervised classification with graph convolutional networks. *International Conference on Learning Representations*.
6. George N. Korres, Nikos D. Hatziargyriou, and Panagiotis J. Katsikas. 2011. State estimation in distribution systems with embedded medium-voltage/low-voltage transformers. *European Transactions on Electrical Power*, 21(2), 1178–1199. https://doi.org/10.1002/etep.442
7. Lalit Kumar and Pooja K. Kherdikar. 2021. An overview of different static state estimation techniques with bad data detection, identification and elimination in power system. *International Journal of Ambient Energy*, 43(1), 4305–4309. https://doi.org/10.1080/01430750.2021.1874524
8. Nikolaos M. Manousakis and George N. Korres. 2021. A framework for distribution-system state estimation with a 55-bus benchmark. *Energies*, 14(23), 7933. https://doi.org/10.3390/en14237933
9. Ricardo Martínez-Parrales, Claudio R. Fuerte-Esquivel, and B. A. Alcaide-Moreno. 2020. Analysis of bad data in power system state estimation under non-Gaussian measurement noise. *Electric Power Systems Research*, 186, 106424. https://doi.org/10.1016/j.epsr.2020.106424
10. Steffen Meinecke et al. 2020. SimBench—a benchmark dataset of electric power systems to compare innovative solutions based on power flow analysis. *Energies*, 13(12), 3290.
11. Shiva Moshtagh, Behrouz Azimian, Mohammad Golgol, and Anamitra Pal. 2025. Topology-aware graph neural network-based state estimation for PMU-unobservable power systems. *IEEE Transactions on Power Systems*, 40(6), 4547–4560. https://doi.org/10.1109/TPWRS.2025.3572848
12. Quang-Ha Ngo, Bang L. H. Nguyen, Tuyen V. Vu, Jianhua Zhang, and Tuan Ngo. 2024. Physics-informed graphical neural network for power system state estimation. *Applied Energy*, 358, 122602. https://doi.org/10.1016/j.apenergy.2023.122602
13. Fred C. Schweppe and John Wildes. 1970. Power system static-state estimation, Part I: Exact model. *IEEE Transactions on Power Apparatus and Systems*, PAS-89(1), 120–125.
14. Petar Veličković et al. 2018. Graph attention networks. *International Conference on Learning Representations*.
15. Huayi Wu, Zhao Xu, Ming-Hao Wang, and Xue Lyu. 2025. Meta-learning enhanced physics-informed graph attention convolutional network for distribution power system state estimation. *IEEE Transactions on Network Science and Engineering*, 12(2), 1186–1197. https://doi.org/10.1109/TNSE.2025.3525625
