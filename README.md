<h1>matrix-processing-benchmark</h1>
<p>Benchmark for comparing Python threading and multiprocessing performance on large matrices</p>
<h2>Project description</h2>
<p>This project:</p>
 <ol>
  <li>Generates a large matrix of random numbers.</li>
  <li>
    <dl>
      <dt>Processes it in two ways:</dt>
      <dd>Threads (<b>threading</b>)</dd>
      <dd>Processes (<b>multiprocessing</b>)</dd>
    </dl>
  </li>
  <li>Measures the execution time of each method.</li>
  <li>Saves the results to a file `results.txt` on the desktop, adding each measurement to the history.</li>
</ol>
<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">matrix-processing-benchmark</th>
  </tr>
  <tr>
    <td>matrix_generator.py</td>
    <td>Matrix generation</td>
  </tr>
  <tr>
    <td>threading_processor.py</td>
    <td>Thread processing</td>
  </tr>
  <tr>
    <td>multiprocessing_processor.py</td>
    <td>Processing</td>
  </tr>
  <tr>
    <td>results_saver.py</td>
    <td>Saving results to TXT</td>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Main launch file</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Project description</td>
  </tr>
</table>
<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone the repository</dt>
        <dd>
          <code>git clone <a href>https://github.com/Kyoryuu-lab/matrix-processing-benchmark.git</a></code>
        </dd>
        <dd>
          <code>cd matrix-processing-benchmark</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install num2words</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Launch a project</dt>
        <dd>
          <code>python main.py</code>
        </dd>
      </dl>
    </li>
  </b>
</ol>
<h2>Example of console output</h2>
<samp>
  <p>
    [INFO] Generating matrix...<br />
    [INFO] Launching Threading...<br />
    [RESULT] Threading time: 12.345678 seconds<br />
    [INFO] Launching Multiprocessing...<br />
    [RESULT] Multiprocessing time: 10.987654 seconds<br />
    [INFO] Results added to /Users/username/Desktop/results.txt
  </p>
</samp>
<h2>Example results.txt file</h2>
<samp> 
  <p>
    === Test from 2025-08-13 14:32:01 ===<br />
    Threading time: 12.345678 seconds<br />
    Multiprocessing time: 10.987654 seconds<br />
    Multiprocessing is faster.<br />
  </p>
</samp>
