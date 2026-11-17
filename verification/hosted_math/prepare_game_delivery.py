#!/usr/bin/env python3
"""Assemble an evidence-bound individual-game handoff from its private checkpoint.

This local formatter reads observations; it never authenticates them, invents
scientific prose, edits a repository, publishes metadata or deletes a chat.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

_SPEC = importlib.util.spec_from_file_location(
    "game_delivery_completion", Path(__file__).with_name("check_completion.py"))
CHECKER = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(CHECKER)
TOPIC = re.compile(r"[a-z0-9][a-z0-9-]{0,49}\Z")
STAGES = ("integrated", "release", "cleanup")
OBJECTIVE_OUTCOMES = {
    "met": "Met",
    "partially_met": "Partially met",
    "not_established": "Not established",
    "not_met": "Not met",
}


def _text(value, label, errors):
    if (not isinstance(value, str) or not value.strip()
            or any(ord(c) < 32 and c not in "\n\r\t" for c in value)):
        errors.append(f"{label}: supply nonempty authored text without control characters")
        return ""
    return value.strip()


def _tasks(delivery, evidence, completion, errors):
    """Use actual stored work, preserving a recorded blocker's exact action."""
    values = delivery.get("pending_tasks", [])
    if not isinstance(values, list):
        errors.append("delivery.pending_tasks: supply a list of actual unfinished tasks")
        values = []
    tasks = []
    for i, value in enumerate(values):
        label = f"delivery.pending_tasks[{i}]"
        if not isinstance(value, dict):
            errors.append(label + ": required task object")
            continue
        if value.get("stage") not in STAGES:
            errors.append(label + ".stage: use integrated, release or cleanup")
        for key in ("reason", "owner", "next_action"):
            _text(value.get(key), label + "." + key, errors)
        tasks.append({key: value.get(key) for key in ("stage", "reason", "owner", "next_action")})
    blocker = evidence.get("blocker")
    if isinstance(blocker, dict) and blocker.get("stage") in STAGES:
        exact = {key: blocker.get(key) for key in ("stage", "reason", "owner", "next_action")}
        for key in ("reason", "owner", "next_action"):
            _text(exact[key], "completion_evidence.blocker." + key, errors)
        conflicting = [t for t in tasks if t["stage"] == exact["stage"] and t != exact]
        if conflicting and exact not in tasks:
            errors.append("delivery.pending_tasks: retain the exact unresolved blocker and its permitted next action")
        if exact not in tasks:
            tasks.insert(0, exact)
    missing = next((s for s in STAGES if not completion["stages"][s]["ok"]), None)
    if missing is not None and not any(t["stage"] == missing for t in tasks):
        errors.append(f"delivery.pending_tasks: record the concrete unfinished {missing} action, reason and responsible owner")
    for task in tasks:
        stage = task["stage"]
        if stage in STAGES and completion["stages"][stage]["ok"]:
            errors.append(f"delivery.pending_tasks: reconcile completed {stage} evidence with its stale unfinished task before delivery")
    return tasks


def _unfinished(tasks):
    return "\n".join(
        f"- {task['reason']} Owner: {task['owner']}. Next action: {task['next_action']}"
        for task in tasks)


def _source_commits(evidence, completion, main):
    """Reuse only the checker's validated same-tree integration path."""
    allowed = {main.get("commit")}
    if not completion["science_integrated"]:
        return allowed
    revision = evidence["revision"]
    integration = evidence["integration"]
    pr = integration["pull_request"]
    edges = [(edge["from_commit"], edge["to_commit"])
             for edge in integration.get("unchanged_descendants", [])]
    allowed.update(CHECKER.Evidence.path_nodes(revision["commit"], pr["head_sha"], edges))
    allowed.update(CHECKER.Evidence.path_nodes(pr["merge_commit_sha"], main["commit"], edges))
    return allowed


def _current_status(root, evidence, completion):
    """Derive one view from current evidence, without promoting old prose flags.

    Recorded tasks are not permission or dependency evidence. A blocker keeps
    its exact action and does not turn other tasks into a global pause.
    """
    game = evidence.get("game")
    game = game if isinstance(game, dict) else {}
    integration = evidence.get("integration")
    integration = integration if isinstance(integration, dict) else {}
    main = integration.get("main")
    main = main if isinstance(main, dict) else {}
    delivery = root.get("delivery")
    delivery = delivery if isinstance(delivery, dict) else {}
    errors = []
    for outer, inner in (("repository", "repository"), ("game_id", "id")):
        if outer in delivery and delivery[outer] != game.get(inner):
            errors.append(f"delivery.{outer}: stored task identity disagrees with the current game")
    if "source_tree" in delivery and delivery["source_tree"] != main.get("tree"):
        errors.append("delivery.source_tree: stored tasks need reconciliation with the inspected source tree")
    if ("source_commit" in delivery
            and (not isinstance(delivery["source_commit"], str)
                 or delivery["source_commit"] not in _source_commits(evidence, completion, main))):
        errors.append("delivery.source_commit: stored tasks need reconciliation with the inspected source revision")
    tasks = _tasks(delivery, evidence, completion, errors)
    missing = next((s for s in STAGES if not completion["stages"][s]["ok"]), None)
    status = {None: "complete", "cleanup": "preservation_pending",
              "release": "release_incomplete", "integrated": "integration_incomplete"}[missing]
    next_task = next((task for task in tasks if task["stage"] == missing
                      and all(isinstance(task.get(k), str) and task[k].strip()
                              for k in ("reason", "owner", "next_action"))), None)
    if errors:
        next_task = None
    blocker = evidence.get("blocker")
    return {
        "workflow_status": status,
        "repository": game.get("repository"), "game_id": game.get("id"),
        "inspected_source": {key: main.get(key) for key in ("commit", "tree", "record", "observed_at")},
        "science_integrated": completion["science_integrated"],
        "repository_ready": completion["release_ready"],
        "chat_cleanup_ready": completion["chat_cleanup_ready"],
        "preservation_exit_ready": completion["preservation_ready"],
        "next_stage": missing, "next_action": next_task,
        "remaining_tasks": tasks,
        "blocker": ({key: blocker.get(key) for key in ("stage", "reason", "owner", "next_action")}
                    if isinstance(blocker, dict) else None),
        "reconciliation_errors": errors,
        "evidence_errors": {stage: completion["stages"][stage]["errors"] for stage in STAGES},
        "scope": completion["scope"],
    }


def status_summary(checkpoint, *, now=None, max_age_hours=24, reports=None):
    """Diagnose evidence and remaining work without requiring delivery metadata.

    No evidence is edited and no operation is authorized or executed. Explicit
    stale tasks/blockers remain visible for the coordinator to reconcile.
    """
    completion = CHECKER.evaluate(checkpoint, now=now, max_age_hours=max_age_hours,
                                  reports=reports)
    root = checkpoint if isinstance(checkpoint, dict) else {}
    evidence = root.get("completion_evidence")
    evidence = evidence if isinstance(evidence, dict) else {}
    current = _current_status(root, evidence, completion)
    labels = {
        "complete": "Current completion evidence passes for the normal game finish.",
        "preservation_pending": "Repository checks passed; preservation remains incomplete.",
        "release_incomplete": "Science is integrated; repository review remains incomplete.",
        "integration_incomplete": "Scientific integration is not yet verified.",
    }
    parts = [labels[current["workflow_status"]]]
    if current["repository"]:
        parts.append(f"Repository: {current['repository']}.")
    source = current["inspected_source"]
    if source["commit"] or source["tree"]:
        parts.append(f"Inspected source: commit {source['commit']}; tree {source['tree']}.")
    if current["remaining_tasks"]:
        parts.append("Recorded remaining work:\n\n" + _unfinished(current["remaining_tasks"]))
    if current["reconciliation_errors"]:
        parts.append("Reconcile the current task record:\n\n" + "\n".join(
            "- " + error for error in current["reconciliation_errors"]))
    return {"ok": completion["chat_cleanup_ready"] and not current["reconciliation_errors"],
            "status": current["workflow_status"], "status_only": True,
            "current_status": current, "completion": completion,
            "errors": current["reconciliation_errors"], "markdown": "\n\n".join(parts) + "\n"}


def prepare(checkpoint, *, now=None, max_age_hours=24, reports=None):
    """Return format errors, unchanged completion verdicts and permitted Markdown.

    An incomplete status can have useful Markdown while ``ok`` remains false.
    Metadata is only rendered when the existing release verdict passes.
    """
    completion = CHECKER.evaluate(checkpoint, now=now, max_age_hours=max_age_hours,
                                  reports=reports)
    errors = []
    root = checkpoint if isinstance(checkpoint, dict) else {}
    evidence = root.get("completion_evidence")
    evidence = evidence if isinstance(evidence, dict) else {}
    current = _current_status(root, evidence, completion)
    game = evidence.get("game")
    game = game if isinstance(game, dict) else {}
    delivery = root.get("delivery")
    if not isinstance(delivery, dict):
        return {"ok": False, "status": "invalid", "markdown": "",
                "errors": ["delivery: add the authored, revision-bound delivery fields to the existing checkpoint"],
                "completion": completion, "current_status": current}
    if type(delivery.get("schema_version")) is not int or delivery.get("schema_version") != 1:
        errors.append("delivery.schema_version: must be 1")
    for outer, key in (("repository", "repository"), ("game_id", "id")):
        value = _text(delivery.get(outer), "delivery." + outer, errors)
        if value != game.get(key):
            errors.append(f"delivery.{outer}: must match completion_evidence.game.{key}")
    integration = evidence.get("integration")
    integration = integration if isinstance(integration, dict) else {}
    main = integration.get("main")
    main = main if isinstance(main, dict) else {}
    allowed_commits = _source_commits(evidence, completion, main)
    for name, field in (("source_commit", "commit"), ("source_tree", "tree")):
        matches = (delivery.get(name) in allowed_commits if field == "commit" and isinstance(delivery.get(name), str)
                   else delivery.get(name) == main.get(field))
        if (not isinstance(delivery.get(name), str)
                or not CHECKER.SHA.fullmatch(delivery[name])
                or not matches):
            errors.append(f"delivery.{name}: must match the inspected scientific main or its validated same-tree integration {field}")
    if "claim_synopsis_record" in delivery:
        _text(delivery["claim_synopsis_record"], "delivery.claim_synopsis_record", errors)
    outcome_text = None
    if "objective_outcome" in delivery:
        outcome = delivery["objective_outcome"]
        if not isinstance(outcome, dict):
            errors.append("delivery.objective_outcome: supply an authored status and explanation")
        else:
            label = OBJECTIVE_OUTCOMES.get(outcome.get("status")) if isinstance(outcome.get("status"), str) else None
            if label is None:
                errors.append("delivery.objective_outcome.status: use met, partially_met, not_established or not_met")
            explanation = _text(outcome.get("explanation"), "delivery.objective_outcome.explanation", errors)
            if label and explanation:
                outcome_text = f"**Original objective:** {label}. {explanation}"
    tasks = _tasks(delivery, evidence, completion, errors)
    release_ready = completion["release_ready"]
    if release_ready:
        result = _text(delivery.get("result"), "delivery.result", errors)
        description = _text(delivery.get("description"), "delivery.description", errors)
        topics = delivery.get("topics")
        if (not isinstance(topics, list) or not 1 <= len(topics) <= 5
                or any(not isinstance(t, str) or not TOPIC.fullmatch(t) for t in topics)):
            errors.append("delivery.topics: supply one to five lowercase scientific GitHub topic slugs, each at most 50 characters")
            topics = []
        if len(topics) != len(set(topics)):
            errors.append("delivery.topics: remove duplicate topics")
        limits = delivery.get("verification_limits")
        if not isinstance(limits, list):
            errors.append("delivery.verification_limits: supply a list; [] means no additional material limitation")
            limits = []
        for i, limit in enumerate(limits):
            _text(limit, f"delivery.verification_limits[{i}]", errors)
    if errors:
        return {"ok": False, "status": "invalid", "markdown": "",
                "errors": errors, "completion": completion, "current_status": current}
    repository = game["repository"]
    if not release_ready:
        status = ("Science is integrated; the normal game finish remains incomplete."
                  if completion["science_integrated"] else
                  "Scientific integration is not yet verified; the normal game finish remains incomplete.")
        anchor = ("\n\nEducational-anchor selection remains pending."
                  if not isinstance(game.get("anchor"), str) or not game["anchor"].strip() else "")
        markdown = f"{status}\n\nRepository: {repository}.{anchor}\n\nRemaining work:\n\n{_unfinished(tasks)}\n"
        return {"ok": False, "status": "incomplete", "markdown": markdown,
                "errors": [], "completion": completion, "current_status": current}
    cleanup_ready = completion["chat_cleanup_ready"]
    lead = ("Completed." if cleanup_ready else
            "Repository checks passed; the normal game finish remains incomplete.")
    parts = [lead, result]
    if outcome_text:
        parts.append(outcome_text)
    parts += [f"**Suggested description**\n\n{description}",
             "**Suggested topics**\n\n" + ", ".join(f"`{topic}`" for topic in topics)]
    if limits:
        parts.append("**Verification limits**\n\n" + "\n".join("- " + item.strip() for item in limits))
    if cleanup_ready:
        handoff = evidence["handoff"]
        receipt = handoff["remote_readback"]
        url = ("https://github.com/GoGoKo699/Camelot/tree/" + receipt["commit"] + "/"
               + quote(handoff["path"].rstrip("/"), safe="/"))
        parts.append(f"Verified Camelot handoff: [saved record]({url}).")
        parts.append("You may delete this originating chat and the associated workspace material explicitly covered by that handoff, while retaining the scientific repository.")
    else:
        parts.append("**Remaining preservation work**\n\n" + _unfinished(tasks))
    return {"ok": True, "status": "complete" if cleanup_ready else "repository_ready",
            "markdown": "\n\n".join(parts) + "\n", "errors": [], "completion": completion,
            "current_status": current}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path, help="Existing private checkpoint with completion_evidence and delivery")
    parser.add_argument("--now", help="Timezone-aware ISO timestamp for reproducible checks")
    parser.add_argument("--max-age-hours", type=float, default=24)
    parser.add_argument("--output", type=Path, help="Save the permitted Markdown response locally")
    parser.add_argument("--json", action="store_true", help="Print the verdict and Markdown as JSON")
    parser.add_argument("--status-only", action="store_true",
                        help="Diagnose current evidence and saved work without requiring final delivery metadata")
    args = parser.parse_args()
    try:
        data = CHECKER.parse_json(args.checkpoint.read_text(encoding="utf-8"))
        reports = CHECKER.load_report_bytes(args.checkpoint, data)
        assemble = status_summary if args.status_only else prepare
        result = assemble(data, now=CHECKER.timestamp(args.now) if args.now else None,
                          max_age_hours=args.max_age_hours, reports=reports)
        if args.output and result["markdown"]:
            # Exclusive creation also refuses existing symlinks, checkpoints,
            # reports and unrelated files without following or overwriting them.
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(result["markdown"])
    except (OSError, UnicodeError, ValueError, TypeError, OverflowError) as exc:
        print(json.dumps({"ok": False, "status": "invalid", "errors": [str(exc)]}))
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["markdown"]:
        print(result["markdown"], end="")
    else:
        for error in result["errors"]:
            print(error, file=sys.stderr)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
