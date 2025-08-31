/**
 * Author: Suhail Al-aboud
 * Email: 10675@holbertonstudents.com
 */

 // Function that executes a math function and handles errors with guardrail
export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // Try executing the math function and push its result
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // If an error occurs, push the error message
    queue.push(`Error: ${error.message}`);
  } finally {
    // Always append the guardrail message
    queue.push('Guardrail was processed');
  }

  return queue;
}
