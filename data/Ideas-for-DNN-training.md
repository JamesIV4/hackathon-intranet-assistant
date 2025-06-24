Why this page?| To jot down ideas that are worth exploring. These are collected by conversations, informal discussions within the group.  
---|---  
Contributors| , ,   
  
 

  1. Replace LDA matrix with a neural network. Does this Introduce non-linearity to the discriminative transform?
  2. Use computationally inexpensive sigmoid function.  
  
  

     * using x / (1 + abs(x)) seems to be the cheapest.  In SSE/AVX this can be computed efficiently as: x / (1 + max(x, 0 - x)).  Likely even better: use ANDPS instruction to mask sign: x / (1 + (x & 0x7fffffff))  

     * SSE/AVX has instructions for square root (SQRTPS/SQRTPD), so we can also test: x / sqrt(1 + x*x).  It furthermore has a "reciprocal of square root" instruction for single precision floats (RSQRTPS), so it's worth comparing against x * rsqrt(1 + x*x) and compare execution cost.  

  3. Quantize the sigmoid function into levels. Try step function to get a binary representation.
  4. Use of double -> float. Does use of float create any quantization issues?
  5. Test posterior probabilities after perturbing inputs.
  6. Can we use the binary feature representation used in finger-printing? diff of mel-filter-bank energies.
  7. Check sensitivity of the learned NN parameters by adding noise to the parameters (not the input) and test impact on classification.  We want to make sure the learned network is stable.
  8. Design network architecture to have more structure and provide additional hints while training. 
     * For example, create a special hidden layers of size 40 (or num monophones) and train the network such that the special layer learns monophone labels and the output layer learns the triphone labels.
     * As an alternative, we could set one of the hidden layers to learn the tied-state labels - and the output layer to learn monophone labels. If this predict monophones accurately - search would be super simple .  
  



