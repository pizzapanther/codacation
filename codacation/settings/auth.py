import os

AUTH_USER_MODEL = 'account.User'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
  'social_core.backends.github.GithubOAuth2',
  
  'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = os.environ.get('GITHUB_KEY', '')
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get('GITHUB_SECRET', '')

SOCIAL_AUTH_GITHUB_SCOPE = ['repo', 'user:email']
