# UCSD-Catalog-API


## Endpoints:
 # GET /health -> simple health check
 - GET /departments -> list of departments (returns id, name, code)
 - GET /search?q=term -> basic search across course titles and department names
 - GET /departments/by-code/<dept_code> -> lookup a department object by its code (case-insensitive)
 - GET /departments/code/<dept_code>/courses -> list courses for the department identified by code
 - GET /departments/code/<dept_code>/courses/<course_number>/sections -> list sections for the given department code
	 and course_number. If multiple course rows share the same course_number in the DB, sections from all
	 matching course rows will be returned and each section will include the numeric `course_id`.