def topologicalSort(jobs, deps):
	jobGraph = createJobGraph(jobs, deps)
	return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
	# Make the graph.
	graph = JobGraph(jobs)
	# Iterate over the tuples and add the prereq to the graph
	for prereq, job in deps:
		graph.addPrereq(job, prereq)
	return graph

def getOrderedJobs(graph):
	orderedJobs = []
	nodes = graph.nodes
	# Iterate throough all the nodes, looking for a cycle.
	while len(nodes):
		node = nodes.pop()
		# Pass the node and the oderedJobs list to the dft
		containsCycle = depthFirstTraverse(node, orderedJobs)
		if containsCycle:
			return []
	# If we make it here, we have an ordered list and that is returned
	return orderedJobs

def depthFirstTraverse(node, orderedJobs):
	if node.visited:
		return False
	if node.visiting:
		return True
	node.visiting = True
	for prereqNode in node.prereqs:
		containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
		if containsCycle:
			return True
	node.visited = True
	node.visiting = False
	orderedJobs.append(node.job)

class JobGraph:
	def __init__(self, jobs):
		self.nodes = []
		self.graph = {} # Graph is a hash so they can be fetched in constant time.
		# Keys are job pointing to the job's created JobNode instance

		# Add all the nodes at the time if graph instantiation.
		for job in jobs:
			self.addNode(job) 

	def addPrereq(self, job, prereq):
		jobNode = self.getNode(job)
		prereqNode = self.getNode(prereq)
		jobNode.prereqs.append(prereqNode)

	def addNode(self, job):
		# Create instances of JobNode then append that node to the graph's node list.
		self.graph[job] = JobNode(job)
		self.nodes.append(self.graph[job])

	def getNode(self, job):
		if job not in self.graph:
			self.addNode(job)
		return self.graph[job]

class JobNode:
	def __init__(self, job):
		# Holds reference to original job and a list of prereqs that are added from
		# the addPrereq function on the JobGraph class, then referenced when
		# traversing the graph.
		self.job = job
		self.prereqs = []
		self.visited = False
		self.visiting = False