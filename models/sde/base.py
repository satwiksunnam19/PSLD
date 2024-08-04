""" Abstract SDE classses, Reverse SDEs and VE/VP SDE."""
import abc 

class SDE(abc.ABC):
    """SDE abstract class, Functions are designed for a mini-batch of inputs."""

    def __init__(self,N):
        """
        Construct an SDE. 

        Args: 
        N: number of discretization time steps.
        """
        super().__init__()
        self.N=N
    
    @property
    @abc.abstractmethod
    def T(self):
        """ End time of the SDE."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_score(self,eps,t):
        """ computes the score for the given epsilon value"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def perturb_data(self,x_0,t,noise=None):
        """ add noise to the data point"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def sde(self,x,t):
        """ Return the drift and the diffusion coefficiets"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def reverse_sde(self,x,t,score_fn,probability_flow=False):
        """return the drift and the difussion coef of the reverse-sde"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def cond_marginal_prob(self,x,t):
        """ Parameters to determine the marginal distribution of the SDE, $p_t(x_t|x_0)$."""
        raise NotImplementedError
    
    @abc.abstractmethod
    def prior_sampling(self,shape):
        """ Generate one sample from the prior distribution, p_T(x)$"""
        raise NotImplementedError
            
    @abc.abstractmethod
    def prior_logp(self,z):
        """Compute log-density of the prior distribution.
        Useful for computing the log-likelihood via probability flow ODE.
        Args:
        z:latent code
        Returns: 
        log probablity density
        """
        pass


