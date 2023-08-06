//
//  Formatter.XML.swift
//  SwiftDraw
//
//  Created by Simon Whitty on 31/12/16.
//  Copyright 2020 Simon Whitty
//
//  Distributed under the permissive zlib license
//  Get the latest version from here:
//
//  https://github.com/swhitty/SwiftDraw
//
//  This software is provided 'as-is', without any express or implied
//  warranty.  In no event will the authors be held liable for any damages
//  arising from the use of this software.
//
//  Permission is granted to anyone to use this software for any purpose,
//  including commercial applications, and to alter it and redistribute it
//  freely, subject to the following restrictions:
//
//  1. The origin of this software must not be misrepresented; you must not
//  claim that you wrote the original software. If you use this software
//  in a product, an acknowledgment in the product documentation would be
//  appreciated but is not required.
//
//  2. Altered source versions must be plainly marked as such, and must not be
//  misrepresented as being the original software.
//
//  3. This notice may not be removed or altered from any source distribution.
//

import Foundation

extension XMLFormatter {
  
  struct CoordinateFormatter {
    var delimeter: Delimeter = .space
    var precision: Precision = .capped(max: 5)
    
    enum Precision {
      case capped(max: Int)
      case maximum
    }
    
    enum Delimeter: String {
      case space = " "
      case comma = ","
    }
    
    func format(_ coordinates: DOM.Coordinate...) -> String {
      return coordinates.map { format(Double($0)) }.joined(separator: delimeter.rawValue)
    }

    func format(_ coordinates: Double...) -> String {
      return coordinates.map { format($0) }.joined(separator: delimeter.rawValue)
    }

    func format(_ c: Double) -> String {
      switch precision {
      case .capped(let max):
        return format(c, capped: max)
      default:
        return String(describing: c)
      }
    }
    
    func format(fraction n: Double, maxDigits: Int) -> String {
      assert(n.sign == .plus)
      
      let min = pow(Double(10), Double(-maxDigits)) - Double.ulpOfOne
      
      guard n >= min else {
        return ""
      }
      
      let s = String(format: "%.\(maxDigits)g", n)
      let idx = s.index(s.startIndex, offsetBy: 1)
      return String(s[idx..<s.endIndex])
    }
    
    func format(_ c: Double, capped: Int) -> String {
      let sign: String
      let n: (Double, Double)
      
      if c.sign == .minus {
        sign = "-"
        n = modf(abs(c))
      } else {
        sign = ""
        n = modf(c)
      }
      
      let integer = Int(n.0)
      let fraction = format(fraction: n.1, maxDigits: capped)
      
      return "\(sign)\(integer)\(fraction)"
    }
  }
}
