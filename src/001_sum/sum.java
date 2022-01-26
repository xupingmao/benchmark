class Main {

    private static final int N = 500000;

    private static void bench() {
        long result = 0;
        for (int i = 0; i < N; i++) {
            result += i;
        }

        System.out.println("loops=" + N);
        System.out.println("result=" + result);
    }

    public static void main(String args[]) {
        long t1 = System.currentTimeMillis();
        bench();
        long cost_time = System.currentTimeMillis() - t1;
        System.out.println("cost_time:" + cost_time + "ms");
    }
}