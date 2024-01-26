from Semantics import SemanticRelation


class StepSyncComposition(SemanticRelation):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        initials = []
        for lhs_c in self.lhs.initial():
            for rhs_c in self.rhs.initial():
                 c=lhs_c,rhs_c
                 initials.append(c)
        return initials

    def actions(self, source):
        lhs_source,rhs_source=source
        SyncActions=[]
        lhs_actions=self.actions(lhs_source)
        lhs_action_count=len(lhs_actions)
        for lhs_action in lhs_actions:
            lhs_targets=self.lhs.execute(lhs_action,lhs_source)
            if len(lhs_targets)==0:
                lhs_action_count-=1
        for lhs_target in lhs_targets:
            lhs_step = (lhs_source, lhs_action, lhs_target)
            rhs_actions=self.rhs.actions(lhs_step,rhs_source)
            actions=map(lambda rA:(lhs_step,rA),rhs_actions)
            SyncActions.extend(actions)

        if lhs_action_count == 0:
            lhs_step = lhs_source ,"deadlock",lhs_source
            rhs_actions = self.rhs.actions(lhs_step, rhs_source)
            SyncActions.extend(map(lambda ra: (lhs_step, ra), rhs_actions))

        return SyncActions

    def execute(self, action, source):
        lhs_source, rhs_source = source
        lhs_step, rhs_action = action
        rhs_targets = self.rhs.execute(rhs_action, lhs_step, rhs_source)
        return map(lambda rhs_target: (lhs_step[2], rhs_target),rhs_targets)