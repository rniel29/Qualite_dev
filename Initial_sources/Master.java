import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.ArrayList;
import java.util.List;
/**
 * Creates workers to run the Monte Carlo simulation
 * and aggregates the results.
 */
class Master {
    
    public static class Result {
        public int ntot;
        public int numWorkers;
        public long timeNanos;
        public double pi;
        public double error;
        
        public Result(int ntot, int numWorkers, long timeNanos, double pi, double error) {
            this.ntot = ntot;
            this.numWorkers = numWorkers;
            this.timeNanos = timeNanos;
            this.pi = pi;
            this.error = error;
        }
    }
    
    public Result doRun(int totalCount, int numWorkers) throws InterruptedException, ExecutionException 
    {

	long startTime = System.nanoTime();

	// Create a collection of tasks
	List<Callable<Long>> tasks = new ArrayList<Callable<Long>>();
	for (int i = 0; i < numWorkers; ++i) 
	    {
		tasks.add(new Worker(totalCount));
	    }
    
	// Run them and receive a collection of Futures
	ExecutorService exec = Executors.newFixedThreadPool(numWorkers);
	List<Future<Long>> results = exec.invokeAll(tasks);
	long total = 0;
    
	// Assemble the results.
	for (Future<Long> f : results)
	    {
		// Call to get() is an implicit barrier.  This will block
		// until result from corresponding worker is ready.
		total += f.get();
	    }
	double pi = 4.0 * total / totalCount / numWorkers;

	long stopTime = System.nanoTime();
    long time = (stopTime - startTime);
    double error = Math.abs((pi - Math.PI)) / Math.PI;
    int ntot = totalCount * numWorkers;
    
	System.out.println("\nPi : " + pi );
	System.out.println("Error: " + error + "\n");

	System.out.println("Ntot: " + ntot);
	System.out.println("Available processors: " + numWorkers);
	System.out.println("Time Duration (nanoseconds): " + time + "\n");

	System.out.println(error + " " + ntot + " " + numWorkers + " " + time);

	exec.shutdown();
    
	return new Result(ntot, numWorkers, time, pi, error);
    }
}