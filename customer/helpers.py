from inventory.models import SuperCategory, CircleCategory, MainBanner, SubBanner, MobileBanner, LeftImageContainer, LeftContainerSubImages, RightImageContainer, RightContainerSubImages
from inventory.serializers import CircleCategorySerializer, MainBannerSerializer
import json

def get_super_categories():
    super_categories = SuperCategory.objects.prefetch_related('category_set__subcategory_set').all()

    data = {
        "super_categories": []
    }

    for super_category in super_categories:
        super_category_data = {
            "name": super_category.name,
            "is_active": super_category.is_active,
            "image_url": super_category.image.url if super_category.image else None,
            "categories": []
        }

        for category in super_category.category_set.all():
            category_data = {
                "name": category.name,
                "sub_categories": []
            }

            for sub_category in category.subcategory_set.all():
                sub_category_data = {"name": sub_category.name}
                category_data["sub_categories"].append(sub_category_data)

            super_category_data["categories"].append(category_data)

        data["super_categories"].append(super_category_data)
    drop_down_data = data
    return drop_down_data


def get_circle_categories():
    circle_categories = CircleCategory.objects.all()
    serializer = CircleCategorySerializer(circle_categories, many=True)
    circle = serializer.data
    circle_data = json.loads(json.dumps(circle))
    return circle_data


def get_active_banners():
    active_banners = MainBanner.objects.filter(active=True)
    banner = MainBannerSerializer(active_banners, many=True)
    banner = banner.data
    banner_data = json.loads(json.dumps(banner))
    return banner_data

def get_subbanner():
    active_sub_banners = SubBanner.objects.filter(active=True)
    sub_banner_urls = {}
    for sub_banner in active_sub_banners:
        sub_banner_urls[sub_banner.id] = {
            'image_url': sub_banner.image.url,
            'alternate_text': sub_banner.alternate_text,
        }
    return sub_banner_urls

def get_mobile_banners():
    active_mobile_banners = MobileBanner.objects.filter(active=True)
    mobile_banners_urls = {}
    for mobile_banner in active_mobile_banners:
        mobile_banners_urls[mobile_banner.id] = {
            'image_url': mobile_banner.image.url,
            'alternate_text': mobile_banner.alternate_text,
        }
    return mobile_banners_urls

def get_left_containers():
    active_left_containers = LeftImageContainer.objects.filter(is_active=True)
    left_containers_urls = {}
    for left_container in active_left_containers:
        left_containers_urls[left_container.id] = {
            'name' : left_container.name,
            'image_url': left_container.image.url,
            'alternate_text': left_container.alternate_text,
        }

    return left_containers_urls

def get_left_sub_images():
    active_left_sub_images = LeftContainerSubImages.objects.filter(is_active=True)
    left_sub_images_urls = {}
    for left_sub_image in active_left_sub_images:
        left_sub_images_urls[left_sub_image.id] = {
            'title': left_sub_image.title,
            'image_url': left_sub_image.image.url,
            'alternate_text': left_sub_image.alternate_text,
        }

    return left_sub_images_urls

def get_right_containers():
    active_right_containers = RightImageContainer.objects.filter(is_active=True)
    right_containers_urls = {}
    for right_container in active_right_containers:
        right_containers_urls[right_container.id] = {
            'name': right_container.name,
            'image_url': right_container.image.url,
            'alternate_text': right_container.alternate_text,
        }

    return right_containers_urls

def get_right_sub_images():
    active_right_sub_images = RightContainerSubImages.objects.filter(is_active=True)
    right_sub_images_urls = {}
    for right_sub_image in active_right_sub_images:
        right_sub_images_urls[right_sub_image.id] = {
            'title': right_sub_image.title,
            'image_url': right_sub_image.image.url,
            'alternate_text': right_sub_image.alternate_text,
        }

    return right_sub_images_urls