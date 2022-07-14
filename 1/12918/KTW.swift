//
//  main.swift
//  algorithm_1
//
//  Created by 김태원 on 2022/07/14.
//

//12918
import Foundation

func solution(_ s:String) -> Bool {
    let c = s.count
    if c == 4 || c == 6{
        return Int(s) != nil
    }
    return false
}

