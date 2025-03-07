include <roundedcube.scad>

$fn=80;
/*translate([30,0,0])difference() {
  roundedcube([30+2,40+2,15],radius=3);
  translate([1,1,1])roundedcube([30,40,20],radius=2);
  translate([9,5,0])rotate([90,0,0]) roundedcube([15,7,10],radius=2);
  translate([21,46,2])rotate([90,0,0]) cube([3,16,9]);
}
*/

difference() {
  roundedcube([30-1,40-1,20],radius=3);
  translate([1,1,1])roundedcube([30-3,40-3,30],radius=2);
  translate([0,0,8])cube(50);
  translate([8,16,0]) cylinder(d=7,h=10);
  }
