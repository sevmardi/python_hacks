import java.io._
import scala.util.control._
import java.util.Date

class Point(val xc: Int, val yc: Int) {
  var x: Int = xc
  var y: Int = yc

  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
    println("Point x location : " + x);
    println("Point y location : " + y);
  }
}

object Demo {
  def main(args: Array[String]) {

  val multiplier = (i:Int) => i * 10

  }



  



}
