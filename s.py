public class BubbleSort {
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    // 示例调用
    public static void main(String[] args) {
        int[] numbers = {64, 34, 25, 12, 22};
        sort(numbers);
        System.out.println("排序后: " + Arrays.toString(numbers)); // 输出：[12, 22, 25, 34, 64]
    }
}
