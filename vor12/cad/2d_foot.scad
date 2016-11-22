// A base board for the VoR-12 project
// This 2D OpenSCAD file can be used with a laser cutting machine or a CNC

// The MIT License
//
// Copyright (c) 2015 Jeremie DECOCK (http://www.jdhp.org)
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

// To export this file to the DXF format:
//
//    openscad -o 2d_foot.dxf 2d_foot.scad
// 
// Requirement: openscad
// Base unit: mm

module 2d_foot() {
    $fn=50;

    inner_square_size = 33;
    outer_square_size = 105;
    screw_hole_diameter = 3;

    difference() {
        union() {
            square(outer_square_size, center=true);
            rotate(45) 2d_toe();
            rotate(135) 2d_toe();
            rotate(-45) 2d_toe();
            rotate(-135) 2d_toe();
        }

        union() {
            square(inner_square_size, center=true);
            translate([-31.5,    0]) circle(d=screw_hole_diameter);
            translate([ 31.5,    0]) circle(d=screw_hole_diameter);
            translate([    0, 38.5]) circle(d=screw_hole_diameter);
        }
    }
}

module 2d_toe() {
    $fn=50;

    toe_depth = 25;
    toe_length = 80;

    hull() {
        square(toe_depth, center=true);
        translate([toe_length, 0]) circle(d=toe_depth);
    }
}

2d_foot();
