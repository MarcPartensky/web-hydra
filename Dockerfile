FROM nixos/nix

RUN nix-env -i python
RUN nix-env -i hydra
