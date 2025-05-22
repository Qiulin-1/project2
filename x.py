// 使用 Set 和扩展运算符去重
function uniqueArray(arr) {
    return [...new Set(arr)];
}

// 示例调用
const numbers = [1, 2, 2, 3, 3, 3];
console.log(uniqueArray(numbers)); // 输出：[1, 2, 3]
