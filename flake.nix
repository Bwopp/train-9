{
  description = "Flakes are good";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        python = pkgs.python314.override {
          packageOverrides = self: super: {
            opencv4 = super.opencv4.override {
              enableGtk2 = true;
              enableGtk3 = true;
            };
          };
        };

        pythonEnv = python.withPackages (ps: with ps; [
          ultralytics
          opencv4
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            pythonEnv
            pkgs.gtk2
            pkgs.gtk3
            pkgs.glib
          ];
        };
      });
}