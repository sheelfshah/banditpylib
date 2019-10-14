```
 _                     _ _ _               _ _ _     
| |                   | (_) |             | (_) |    
| |__   __ _ _ __   __| |_| |_ _ __  _   _| |_| |__  
| '_ \ / _` | '_ \ / _` | | __| '_ \| | | | | | '_ \ 
| |_) | (_| | | | | (_| | | |_| |_) | |_| | | | |_) |
|_.__/ \__,_|_| |_|\__,_|_|\__| .__/ \__, |_|_|_.__/ 
                              | |     __/ |          
                              |_|    |___/                
```

A python library for bandit algorithms.

## TODO

* add MNL bandit

## Features

* support multiprocesses
* easy to extend

## Implemented Algorithms

### Classic Bandit

#### regret minimization

* Uniform
* Epsilon Greedy
* UCB [[1]](#ACF02)
* MOSS [[2]](#AB09)
* Thompson Sampling \[[3](#T33), [4](#KKM12)\]

## Example

![output example](figures/example.jpg)

See [main.py](main.py) for details.

## Requirement

See [requirements.txt](requirements.txt) for details.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

* This project is inspired by [libbandit](https://github.com/tor/libbandit) and [banditlib](https://github.com/jkomiyama/banditlib) which are both c++ libraries for bandit algorithms.
* This readme file is following the style of [README-Template.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
* The title is generated by [TAAG](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20).

## References

1. <a name="ACF02"></a> Peter Auer, Nicolo Cesa-Bianchi, and Paul Fischer. Finite-time analysis of the multiarmed bandit problem. Machine learning, pages 235–256, 2002.
2. <a name="AB09"></a> Jean-Yves Audibert and Sébastien Bubeck. Minimax Policies for Adversarial and Stochastic Bandits. In COLT, 2009.
3. <a name="T33"></a> William R Thompson. On the likelihood that one unknown probability exceeds another in view of the evidence of two samples. Biometrika, 25(3/4):285–294, 1933.
4. <a name="KKM12"></a> Emilie Kaufmann, Nathaniel Korda, and Rémi Munos. Thompson sampling: An asymptotically optimal finite-time analysis. In ALT, pages 199–213, 2012.
