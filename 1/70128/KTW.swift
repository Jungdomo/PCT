//
//  main.swift
//  algorithm_1
//
//  Created by 김태원 on 2022/04/20.
//

import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    
    let len = a.count
    var result = 0
    
    for i in 0..<len{
        result += a[i]+b[i]
    }
    
    return result
}
