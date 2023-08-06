# QrPypi
Python QR Code generator.

## Installation

pip install qrpypi

## What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

## Usage

from qrpypi import qrcode

x = qrcode.make("your url / text")

ex.
x = qrcode.make("acnsoft.net")
