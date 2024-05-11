import numpy as np
import gym

class adaptiveKanervaCoder:
    def __init__(self, observation_space: gym.spaces.Space, st_scale: float, n_prototypes: int, observation_list: np.ndarray,
                 n_closest: int, random_seed):
        """
        Base Kanerva Coder using Selective Kanerva Coding

        :param observation_space: space to approximate
        :param n_prototypes: number of prototypes to represent space
        :param n_closest: number of active prototypes
        """
        self.n_prototypes = n_prototypes
        self.st_scale = st_scale
        self.observation_list = observation_list
        self.dimensions = observation_space.low.shape[0]
        self.observation_space = observation_space
        self.observation_range = observation_space.high - observation_space.low
        self.visit_counts = np.zeros(n_prototypes)
        self.n_closest = n_closest
        self.seed = random_seed
        np.random.seed(self.seed)

        self.prototypes = self.generate_random_prototypes()
    
    def normalize(self, data: np.ndarray) -> np.ndarray:
        """
        Normalizes the data to be between 0,1

        :param data: data to normalize
        :return: normalized data
        """
        normed_data = data - self.observation_space.low
        normed_data /= self.observation_range
        return normed_data

    def euclidean_distance(self, data: np.ndarray) -> np.ndarray:
        """
        Computes the distance between the data and the prototypes.
        Defaults to euclidian distance

        :param data:
        :return: array of distance values between the input data and each prototype
        """
        data = self.normalize(data)
        dist = self.prototypes - data
        dist = np.sqrt(sum(dist.T**2))
        return dist

    def manhattan_distance(self, data: np.ndarray) -> np.ndarray:
        """
        Computes the distance between the data and the prototypes.
        Defaults to manhattan distance

        :param data:
        :return: array of distance values between the input data and each prototype
        """
        data = self.normalize(data)
        dist = self.prototypes - data
        dist = sum(abs(dist.T))
        return dist
    
    def get_features(self, data: np.ndarray) -> np.ndarray:
        """
        Gets the active features for the input data. Updates the visit counts

        :param data: input data
        :return: array of active feature indexes
        """
        indexes = np.argpartition(self.euclidean_distance(data), self.n_closest, axis=0)[:self.n_closest]
        self.visit_counts[indexes] += 1
        return indexes

    def get_prototypes(self) -> np.ndarray:
        """
        Gets the prototypes

        :return: array of prototypes
        """
        return self.prototypes
    
    def generate_random_prototypes(self):
        # Initialize an empty list to store the generated points
        generated_points = []
        
        # Generate num_points random points
        for _ in range(self.n_prototypes):
            # Select a random point from observation_list
            selected_point = self.observation_list[np.random.choice(len(self.observation_list))]
            
            # Generate a random point close to the selected point
            random_point = selected_point + np.random.normal(loc=0, scale = self.st_scale, size=2)
            
            # Ensure the generated point is bounded between 0 and 1
            random_point = np.clip(random_point, 0, 1)
            
            # Append the generated point to the list
            generated_points.append(random_point)
        
        return np.array(generated_points)
    

   