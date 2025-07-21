from langchain_openai import ChatOpenAI
from agent.prompts import (
    content_briefing_prompt,
    competitive_analysis_prompt,
    seo_audit_prompt,
    seo_optimization_prompt,
    campaign_plan_prompt,
    seo_lighthouse_prompt,
    landingpage_strategy_prompt,
    monthly_report_prompt,
    tactical_actions_prompt
)
from agent.tools.lighthouse_runner import run_lighthouse
import json

llm = ChatOpenAI(model="gpt-4o")

def run_agent(mode: str, **kwargs):
    if mode == "briefing":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für Briefing")
        prompt = content_briefing_prompt.format(context=context)
        return llm.invoke(prompt).content

    elif mode == "vergleich":
        context_kunde = kwargs.get("text_kunde")
        context_mitbewerber = kwargs.get("text_mitbewerber")
        if not context_kunde or not context_mitbewerber:
            raise ValueError("Beide Texte (Kunde & Mitbewerber) werden benötigt")
        prompt = competitive_analysis_prompt.format(
            context_kunde=context_kunde,
            context_mitbewerber=context_mitbewerber
        )
        return llm.invoke(prompt).content

    elif mode == "seo_audit":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für SEO-Audit")
        prompt = seo_audit_prompt.format(context=context)
        return llm.invoke(prompt).content

    elif mode == "seo_optimize":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für SEO-Optimierung")
        prompt = seo_optimization_prompt.format(context=context)
        return llm.invoke(prompt).content

    elif mode == "campaign_plan":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für Kampagnenplanung")
        prompt = campaign_plan_prompt.format(context=context)
        return llm.invoke(prompt).content

    elif mode == "seo_lighthouse":
        url = kwargs.get("url")
        if not url:
            raise ValueError("URL für Lighthouse-Analyse fehlt.")
        report = run_lighthouse(url)
        seo_data = json.dumps(report["categories"]["seo"], indent=2)
        prompt = seo_lighthouse_prompt.format(context=seo_data)
        return llm.invoke(prompt).content

    elif mode == "landingpage_strategy":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für Landingpage-Strategie")
        prompt = landingpage_strategy_prompt.format(context=context)
        return llm.invoke(prompt).content

    elif mode == "monthly_report":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für Monatsreport")
        prompt = monthly_report_prompt.format(context=context)
        return llm.invoke(prompt).content

    elif mode == "tactical_actions":
        context = kwargs.get("text")
        if not context:
            raise ValueError("Text fehlt für Maßnahmenplanung")
        prompt = tactical_actions_prompt.format(context=context)
        return llm.invoke(prompt).content

    else:
        raise ValueError(f"Unbekannter Modus: {mode}")
