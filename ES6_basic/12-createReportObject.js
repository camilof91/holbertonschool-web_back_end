export default function createReportObject(employeesList) {
    const allEmployees = { ...employeesList };
  
    return {
      allEmployees,
      getNumberOfDepartments: () => Object.keys(allEmployees).length,
    };
  }
