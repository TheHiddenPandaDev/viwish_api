<?php

declare(strict_types=1);

namespace App\Application\Customer\FindByEmailAndDomain;

final class FindByEmailAndDomainQuery
{
    private string $email;
    private string $domain;

    public function __construct(string $email, string $domain)
    {
        $this->email = $email;
        $this->domain = $domain;
    }

    public function email(): string
    {
        return $this->email;
    }

    public function domain(): string
    {
        return $this->domain;
    }
}
