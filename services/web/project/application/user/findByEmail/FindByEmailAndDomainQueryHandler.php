<?php

declare(strict_types=1);

namespace App\Application\Customer\FindByEmailAndDomain;

use App\Domain\Customer\Service\CustomerByEmailAndDomainFinder;

final class FindByEmailAndDomainQueryHandler
{
    private CustomerByEmailAndDomainFinder $finder;

    public function __construct(CustomerByEmailAndDomainFinder $finder)
    {
        $this->finder = $finder;
    }

    public function __invoke(FindByEmailAndDomainQuery $query): FindByEmailAndDomainResponse
    {
        $customer = $this->finder->__invoke($query->email(), $query->domain());

        return (new FindByEmailAndDomainResponseConverter())->__invoke($customer);
    }
}
