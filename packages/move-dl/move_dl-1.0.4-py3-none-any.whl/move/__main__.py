import hydra 
from omegaconf import OmegaConf

from move.conf.schema import MOVEConfig

@hydra.main(config_path="conf", config_name="main")
def main(config: MOVEConfig) -> str:
#     print(config.model.continuous_names)
    print(config.keys())
    print(OmegaConf.to_yaml(config))
    
if __name__ == "__main__":
    main()

