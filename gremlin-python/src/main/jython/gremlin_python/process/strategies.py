'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

__author__ = 'Marko A. Rodriguez (http://markorodriguez.com)'

from gremlin_python.process.traversal import TraversalStrategy


#########################
# DECORATION STRATEGIES #
#########################

class ConnectiveStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class ElementIdStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


# EventStrategy doesn't make sense outside JVM traversal machine

class HaltedTraverserStrategy(TraversalStrategy):
    def __init__(self, halted_traverser_factory=None):
        TraversalStrategy.__init__(self)
        if halted_traverser_factory is not None:
            self.configuration["haltedTraverserFactory"] = halted_traverser_factory


class PartitionStrategy(TraversalStrategy):
    def __init__(self, partition_key=None, write_partition=None, read_partitions=None, include_meta_properties=None):
        TraversalStrategy.__init__(self)
        if partition_key is not None:
            self.configuration["partitionKey"] = partition_key
        if write_partition is not None:
            self.configuration["writePartition"] = write_partition
        if write_partition is not None:
            self.configuration["readPartitions"] = read_partitions
        if include_meta_properties is not None:
            self.configuration["includeMetaProperties"] = include_meta_properties


class SubgraphStrategy(TraversalStrategy):
    def __init__(self, vertices=None, edges=None, vertex_properties=None):
        TraversalStrategy.__init__(self)
        if vertices is not None:
            self.configuration["vertices"] = vertices
        if edges is not None:
            self.configuration["edges"] = edges
        if vertex_properties is not None:
            self.configuration["vertexProperties"] = vertex_properties


class VertexProgramStrategy(TraversalStrategy):
    def __init__(self, graph_computer=None, workers=None, persist=None, result=None, vertices=None, edges=None,
                 configuration=None):
        TraversalStrategy.__init__(self)
        if graph_computer is not None:
            self.configuration["gremlin.graphComputer"] = graph_computer
        if workers is not None:
            self.configuration["gremlin.graphComputer.workers"] = workers
        if persist is not None:
            self.configuration["gremlin.graphComputer.persist"] = persist
        if result is not None:
            self.configuration["gremlin.graphComputer.result"] = result
        if vertices is not None:
            self.configuration["gremlin.graphComputer.vertices"] = vertices
        if edges is not None:
            self.configuration["gremlin.graphComputer.edges"] = edges
        if configuration is not None:
            self.configuration.update(configuration)


###########################
# FINALIZATION STRATEGIES #
###########################

class MatchAlgorithmStrategy(TraversalStrategy):
    def __init__(self, match_algorithm=None):
        TraversalStrategy.__init__(self)
        if match_algorithm is not None:
            self.configuration["matchAlgorithm"] = match_algorithm


###########################
# OPTIMIZATION STRATEGIES #
###########################

class AdjacentToIncidentStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class FilterRankingStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class IdentityRemovalStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class IncidentToAdjacentStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class InlineFilterStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class LazyBarrierStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class MatchPredicateStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class OrderLimitStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class PathProcessorStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class PathRetractionStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class RangeByIsCountStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class RepeatUnrollStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class GraphFilterStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


###########################
# VERIFICATION STRATEGIES #
###########################

class LambdaRestrictionStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)


class ReadOnlyStrategy(TraversalStrategy):
    def __init__(self):
        TraversalStrategy.__init__(self)
