"""
Meta Ads MCP - Python Package

This package provides a Meta Ads MCP integration
"""

# 모듈 임포트 전에 .env를 로드하여 환경 변수 설정
from pathlib import Path as _Path
from dotenv import load_dotenv as _load_dotenv
# meta-ads-mcp 디렉토리의 .env 파일 로드
_pkg_root = _Path(__file__).resolve().parent.parent
_load_dotenv(_pkg_root / ".env")

from meta_ads_mcp.core.server import main

__version__ = "1.0.87"

__all__ = [
    'get_ad_accounts',
    'get_account_info',
    'get_campaigns',
    'get_campaign_details',
    'create_campaign',
    'get_adsets',
    'get_adset_details',
    'update_adset',
    'get_ads',
    'get_ad_details',
    'get_ad_creatives',
    'get_ad_image',
    'update_ad',
    'get_insights',
    # 'get_login_link' is conditionally exported via core.__all__
    'login_cli',
    'main',
    'search_interests',
    'get_interest_suggestions',
    'estimate_audience_size',
    'search_behaviors',
    'search_demographics',
    'search_geo_locations'
]

# Import key functions to make them available at package level
from .core import (
    get_ad_accounts,
    get_account_info,
    get_campaigns,
    get_campaign_details,
    create_campaign,
    get_adsets,
    get_adset_details,
    update_adset,
    get_ads,
    get_ad_details,
    get_ad_creatives,
    get_ad_image,
    update_ad,
    get_insights,
    login_cli,
    main,
    search_interests,
    get_interest_suggestions,
    estimate_audience_size,
    search_behaviors,
    search_demographics,
    search_geo_locations
)

# Define a main function to be used as a package entry point
def entrypoint():
    """Main entry point for the package when invoked with uvx."""
    # .env는 이미 모듈 최상단에서 로드됨
    return main()

# Re-export main for direct access
main = main 