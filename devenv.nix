{ pkgs, ... }:
let
  python = pkgs.python314.override {
    packageOverrides = self: super: {
      opencv4 = super.opencv4.override { enableGtk2 = true; };
    };
  };
in
{
  languages.python = {
    enable = true;
    package = python.withPackages (ps: with ps; [ ultralytics opencv4 ]);
  };
}