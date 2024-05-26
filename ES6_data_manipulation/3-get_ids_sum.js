export default function getIdsSum(students) {
  if (students instanceof Array) {
    return students.reduce((sum, student) => sum + student.id, 0);
  }
  return 0;
}
