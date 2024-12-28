{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = with pkgs; [
      python312
      python312Packages.qrcode
      python312Packages.pillow
    ];

  shellHook = ''
  '';
}
